.PHONY: help test test-crit report report-server clean

help: ## Show available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-20s %s\n", $$1, $$2}'

test: ## Run all tests in Docker
	@docker-compose up --build

test-crit: ## Run critical tests only in Docker
	docker-compose run --rm tests pytest -v -m crit
	docker-compose run --rm tests allure generate allure-results -o allure-report --clean

report: ## Open Allure report in browser
	@if command -v allure >/dev/null 2>&1; then \
		allure serve allure-results; \
	else \
		echo "Allure not installed. Open allure-report/index.html in browser"; \
	fi

report-server: ## Start report server on http://localhost:8080
	docker-compose --profile report up -d
	@echo "Report server started at http://localhost:8080"
	@echo "To stop: docker-compose --profile report down"

clean: ## Clean test results
	rm -rf allure-results allure-report test-results
	docker-compose down --rmi local 2>/dev/null || true
