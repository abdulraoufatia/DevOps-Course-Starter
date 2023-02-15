terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
  backend "azurerm" {
    resource_group_name  = "KPMG21_AbdulraoufAtia_ProjectExercise"
    storage_account_name = "m12storageaccount"
    container_name       = "m12containertf"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "KPMG21_AbdulraoufAtia_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "ARA-TODO-APP"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  site_config {
    application_stack {
      docker_image     = "abdulraoufatia/todoapp"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL"          = "https://index.docker.io",
    "CLIENTID"                            = "${var.CLIENTID}",
    "CLIENTSECRET"                        = "${var.CLIENTSECRET}",
    "FLASK_APP"                           = "todo_app/app:create_app",
    "ID"                                  = "${var.ID}",
    "PRIMARY_CONNECTION_STRING"           = azurerm_cosmosdb_account.db.connection_strings[0],
    "SECRET_KEY"                          = "secret-key",
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
  }

}
resource "azurerm_cosmosdb_account" "db" {
  name                = "md12-cosmos-db"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "uksouth"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "db" {
  name                = "md10-cosmos-db"
  resource_group_name = data.azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.db.name
}


output "cosmosdb_connectionstrings" {
  value     = "AccountEndpoint=${azurerm_cosmosdb_account.db.endpoint};AccountKey=${azurerm_cosmosdb_account.db.primary_key};"
  sensitive = true
}


