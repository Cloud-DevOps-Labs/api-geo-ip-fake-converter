.PHONY: plan apply destroy test

# Terraform commands
plan:
	cd iac && terraform plan

apply:
	cd iac && terraform apply -auto-approve

destroy:
	cd iac && terraform destroy -auto-approve

# Test the API using the curl command from terraform output
test:
	@echo "Testing API..."
	@cd iac && eval "$$(terraform output -raw curl_example)" | jq .
	@echo "\nTesting invalid API key..."
	@cd iac && curl -s "$$(terraform output -raw api_endpoint)?ip=1.2.3.4&api_key=invalid" | jq .
	@echo "\nTesting missing IP..."
	@cd iac && curl -s "$$(terraform output -raw api_endpoint)?api_key=$$(terraform output -raw api_key)" | jq .
