include .env
export

DATABASE_URL := postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)


migrations-apply:
	poetry run yoyo apply --database $(DATABASE_URL) migrations

migrations-rollback:
	poetry run yoyo rollback --database $(DATABASE_URL) migrations

migrations-list:
	poetry run yoyo list --database $(DATABASE_URL) migrations

show-database-url:
	@echo $(DATABASE_URL)
