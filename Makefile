install-model:
	@echo "Installing model..."
	curl -fsSL https://ollama.com/install.sh | sh
	ollama pull gpt-oss:20b
	@echo "Model installed successfully."


lint:
	ruff check .