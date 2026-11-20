# 🧠 Roboldo-IA-Movimento — Inteligência Artificial, Voz & Navegação (Python)

Repositório oficial dos módulos em **Python** responsáveis pela **Inteligência Artificial conversacional (IHR)**, **Síntese e Reconhecimento de Voz (STT / Piper TTS)** e **Algoritmos de Movimento & Navegação Autônoma (SLAM)** do **Roboldo** (incluindo os códigos da **versão 1.0** e evolução para a **versão 2.0**).

---

## 🧭 Divisão Modular por Zonas

1. **`ia_voz/`** (*Zonas 2 & 3 — Voz, Expressividade e IA*):
   - Pipeline de conversação natural (STT Whisper/Groq + LLM com personalidade educativa do Roboldo).
   - Serviço unificado de síntese de voz neural offline (**Piper TTS** `pt-BR`) e marcadores de sincronia labial (*lipsync*).
2. **`movimento_slam/`** (*Zona 1 — SLAM & Navegação Autônoma*):
   - Fusão sensorial (LiDAR, Odometria e IMU) e construção de mapa 2D (*Occupancy Grid*).
   - Planejamento de trajetória (*Path Planning* A* / Dijkstra) e desvio dinâmico de obstáculos.
3. **`v1_legado/`** (*Roboldo v1.0*):
   - Algoritmos em Python de IA e movimentação desenvolvidos na versão 1.0 do Roboldo, preservados para referência, testes comparativos e migração.

---

## 👥 Equipes Responsáveis (`CODEOWNERS`)

- **Zona 1 (SLAM & Movimento)**: `@ROBOLDO-UERN/zona-slam` ([📋 Project Zona 1](https://github.com/orgs/ROBOLDO-UERN/projects/1))
- **Zona 2 (Voz & Piper TTS)**: `@ROBOLDO-UERN/zona-voz` ([📋 Project Zona 2](https://github.com/orgs/ROBOLDO-UERN/projects/2))
- **Zona 3 (IA & IHR)**: `@ROBOLDO-UERN/zona-ia` ([📋 Project Zona 3](https://github.com/orgs/ROBOLDO-UERN/projects/3))
- **Coordenação**: `@ROBOLDO-UERN/professores` & `@ROBOLDO-UERN/bolsistas`
- **Painel Geral da Organização**: [📋 Central Geral de Trabalhos (Project #6)](https://github.com/orgs/ROBOLDO-UERN/projects/6)
