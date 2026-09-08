import { ServerOptions, cli, defineAgent, voice } from '@livekit/agents';
import * as sarvam from '@livekit/agents-plugin-sarvam';
import * as silero from '@livekit/agents-plugin-silero';
import { LLM as OpenAILLM } from '@livekit/agents-plugin-openai';
import dotenv from 'dotenv';
import { fileURLToPath } from 'node:url';
import { createMediKioskAgent } from './agent.ts';

// Load credentials
dotenv.config({ path: '.env.local' });
dotenv.config({ path: '.env' });

const sarvamApiKey = process.env.SARVAM_API_KEY || 'sk_k78xw4hw_AIq2FZ8NytX15FVxcXIdVHcU';

export default defineAgent({
  entry: async (ctx) => {
    // 1. Voice Activity Detector
    const vad = await silero.VAD.load();

    // 2. Multilingual Indic Reasoning LLM (Sarvam 105B)
    const sarvamLLM = new OpenAILLM({
      model: 'sarvam-105b-conversations',
      baseURL: 'https://api.sarvam.ai/v1',
      apiKey: sarvamApiKey,
    });

    // 3. Configure voice session with Sarvam STT (saaras:v3) and TTS (bulbul:v3)
    const session = new voice.AgentSession({
      // Speech to Text: Sarvam Saaras v3 with multilingual Indic auto-detection
      stt: new sarvam.STT({
        apiKey: sarvamApiKey,
        model: 'saaras:v3',
        languageCode: 'unknown',
      }),

      // Text to Speech: Sarvam Bulbul v3 with natural expressive Indic voice
      tts: new sarvam.TTS({
        apiKey: sarvamApiKey,
        model: 'bulbul:v3',
        speaker: 'priya',
      }),

      // LLM Reasoning: Sarvam 105B
      llm: sarvamLLM,

      // Voice Activity Detection
      vad: vad,

      turnHandling: {
        interruption: { mode: 'adaptive' },
        preemptiveGeneration: { enabled: true },
        endpointing: {
          minDelay: 0.35,
          maxDelay: 1.2,
        },
      },
    });

    // Start voice session with MediKiosk Ayush OPD Agent
    await session.start({
      agent: createMediKioskAgent(),
      room: ctx.room,
    });

    // Connect to LiveKit Room
    await ctx.connect();

    // Initial warm greeting in spoken Hindi/Hinglish (instant synthesis without waiting for LLM generation)
    session.say(
      'Namaste Govind ji! Main Dr. Vaidya Ananya Sharma ke OPD se MediKiosk AI clinical assistant hoon. Aapke pair ke ghav aur dawaiyon ka status lene ke liye call kiya hai. Abhi aapke pair ke ghav mein dard kaisa hai?',
      { allowInterruptions: true }
    );
  },
});

// Run LiveKit Agent CLI
cli.runApp(
  new ServerOptions({
    agent: fileURLToPath(import.meta.url),
    agentName: 'medikiosk-voice-agent',
    wsURL: process.env.LIVEKIT_URL,
    apiKey: process.env.LIVEKIT_API_KEY,
    apiSecret: process.env.LIVEKIT_API_SECRET,
    numIdleProcesses: 1,
    initializeProcessTimeout: 60 * 1000,
  }),
);

