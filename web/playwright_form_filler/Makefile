PLAYWRIGHT_DIR := $(HOME)/.cache/ms-playwright
.PHONY: setup run


run: setup
	uv run main.py 

setup:
	@if [ ! -d "$(PLAYWRIGHT_DIR)" ]; then \
		echo "Playwright not installed, installing..."; \
		uv run playwright install; \
	else \
		echo "Playwright already installed, skipping setup."; \
	fi

