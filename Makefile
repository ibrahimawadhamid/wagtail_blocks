help: ## See what commands are available.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'

publish: ## Publishes a new version to pypi.
	DEL /F dist && python setup.py sdist && twine upload dist/* && echo 'Success! Go to https://pypi.python.org/pypi/wagtail-blocks/ and check that all is well.'
