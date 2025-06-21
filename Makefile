include .env
export

DATABASE_URL := postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

.PHONY: apply rollback list show-url

migrations-apply:
	yoyo apply --database $(DATABASE_URL) migrations

migrations-rollback:
	yoyo rollback --database $(DATABASE_URL) migrations

migrations-list:
	yoyo list --database $(DATABASE_URL) migrations

show-database-url:
	@echo $(DATABASE_URL)