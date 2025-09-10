# Open WebUI ↔ LangGraph Pipe 

[![Open WebUI](https://img.shields.io/badge/Open%20WebUI-v0.6.25-blue)](https://docs.openwebui.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph%20SDK-v0.2.6-blue)](https://docs.langchain.com/oss/python/langgraph/overview)

📖 If you haven't already, check out the detailed Medium article explaining this integration: [Read the article](https://pessini.medium.com/from-open-webui-to-langgraph-building-a-human-in-the-loop-pipe-for-real-time-ai-control-26561cca9f9c)

This project demonstrates how to integrate [Open WebUI](https://github.com/open-webui) with [LangGraph](https://github.com/langchain-ai/langgraph) using a custom **Pipe function**.  
Unlike basic integrations, this implementation includes **human-in-the-loop features** such as:

- ✅ Real-time streaming of messages  
- ✅ Handling agent interrupts and resuming with user input (**Human-in-the-Loop - HITL**)
- ✅ Status events for better user feedback  
- ✅ Optional debug logging and tool call visibility  

With this setup, Open WebUI becomes a powerful interface for experimenting with **interactive, controllable AI agents** built on LangGraph.

> ### Get the Pipe function [here](https://openwebui.com/f/pessini/langgraph_hitl).

## How to Run

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
3. Start the LangGraph development server (keep this terminal open):
   ```bash
   langgraph dev --no-reload
   ```
4. Open a new terminal session and start Open WebUI:
   ```bash
   open-webui serve
   ```

> **Note:** Steps 3 and 4 must run in separate terminal sessions so both services remain active.

### Common Issues

- When using Open WebUI, it is recommended to disable the title generation and auto tags features, as they can sometimes cause conflicts with the agent.