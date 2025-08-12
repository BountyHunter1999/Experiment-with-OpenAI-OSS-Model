# Experimenting with OpenAI OSS Model

A comprehensive experiment with OpenAI's open-source models using Ollama, featuring function calling, agents, and visualization capabilities.

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai/) installed
- Network access for model downloads

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Experiment-with-OpenAI-OSS-Model
   ```

2. **Install Python dependencies:**

   ```bash
   # Using uv (recommended)
   uv sync

   ```

3. **Install and setup Ollama model:**
   ```bash
   make install-model
   ```

## 🏃‍♂️ Running the Experiments

### Basic Chat Completion

Run a simple chat completion with the GPT-OSS model:

```bash
python main.py
```

This demonstrates basic usage with a DevOps-focused conversation.

### Agent with Function Tools

Run the agent experiment with weather tool:

```bash
python agent.py
```

### Visualization

Explore the visualization capabilities:

```bash
python viz.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# OpenAI API configuration for Ollama
OPENAI_API_KEY=ollama
BASE_URL=http://localhost:11434/v1

# Optional: Set to true for more verbose logging
DEBUG=false
```

**Important**: When using Ollama, the `OPENAI_API_KEY` should be set to `ollama` (not a real API key), and the `BASE_URL` should point to your Ollama server.

### Ollama Setup

#### Local Development

1. **Start Ollama server:**

   ```bash
   ollama serve
   ```

2. **Test the model:**
   ```bash
   ollama run gpt-oss:20b
   ```

#### Production Deployment

For hosting Ollama on a server:

1. **Create systemd service:**

   ```bash
   sudo cp service.conf /etc/systemd/system/ollama.service
   sudo systemctl daemon-reload
   sudo systemctl enable ollama
   sudo systemctl start ollama
   ```

2. **Configure firewall:**

   ```bash
   # Allow access from local network
   sudo ufw allow from 192.168.2.0/24 to any port 11434

   # Or allow from specific IP
   sudo ufw allow from YOUR_IP_ADDRESS to any port 11434
   ```

3. **Verify service status:**
   ```bash
   sudo systemctl status ollama
   ```

## 🔧 Development

### Code Quality

The project uses `ruff` for linting and formatting:

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Fix issues
ruff check --fix .
```

### Adding New Tools

1. Create a new JSON file in the `tools/` directory
2. Define the function schema following the OpenAI function calling format
3. Import and use in your Python code

### Adding New Models

1. Pull the model with Ollama: `ollama pull model-name`
2. Update the `MODEL` variable in your Python files
3. Test the model: `ollama run model-name`

## 🐛 Troubleshooting

### Common Issues

1. **404 Page Not Found Error:**

   - Ensure your `.env` file has the correct configuration:
     ```bash
     OPENAI_API_KEY=ollama
     BASE_URL=http://localhost:11434/v1
     ```
   - Check that Ollama is running: `ollama list`
   - Verify the model is installed: `ollama pull gpt-oss:20b`
   - Test Ollama directly: `ollama run gpt-oss:20b`

2. **Ollama not responding:**

   - Check if Ollama is running: `ollama list`
   - Restart the service: `sudo systemctl restart ollama`

3. **Model not found:**

   - Pull the model: `ollama pull gpt-oss:20b`
   - Check available models: `ollama list`

4. **Connection refused:**

   - Verify Ollama is listening on the correct port: `netstat -tlnp | grep 11434`
   - Check firewall settings

5. **Python import errors:**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `uv sync`

### Logs

Check Ollama logs:

```bash
sudo journalctl -u ollama -f
```

## 📚 Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Agents](https://github.com/openai/openai-agents)
- [GPT-OSS Model](https://huggingface.co/openai-community/gpt-oss)

---

**Note**: This is an experimental project for learning and testing OpenAI's open-source models. The models and responses may vary in quality and should not be used for production applications without proper evaluation.
