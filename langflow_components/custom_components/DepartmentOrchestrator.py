import requests
import json
from langflow.base.models.model import LCModelComponent
from langflow.field_typing import Text

class DepartmentOrchestrator(LCModelComponent):
    display_name: str = "Department Orchestrator"
    description: str = "Receives PM delegations and calls other agent APIs, then aggregates results."
    icon = "Users"

    def build_config(self):
        return {
            "pm_json_output": {"display_name": "PM JSON Output", "field_type": Text},
            "langflow_base_url": {"display_name": "LangFlow Base URL", "field_type": Text, "value": "http://langflow_service:7860"},
        }

    def build(self, pm_json_output: str, langflow_base_url: str) -> dict:
        try:
            pm_data = json.loads(pm_json_output)
            delegations = pm_data.get("delegations",)
            summary_for_user = pm_data.get("summary_for_user", "The PM did not provide a summary.")
            
            aggregated_results =

            for delegation in delegations:
                department = delegation.get("department")
                task = delegation.get("task")
                
                if not department or not task:
                    aggregated_results.append({
                        "department": department or "Unknown",
                        "status": "error",
                        "response": "Delegation was missing a department or task."
                    })
                    continue

                # Construct the API endpoint for the specialist agent
                # Assumes LangFlow graphs are saved with names like "Art_Agent", "Code_Agent"
                agent_api_url = f"{langflow_base_url}/api/v1/run/{department}?stream=false"
                
                payload = {
                    "input_value": task,
                    "output_type": "chat", 
                    "input_type": "chat"
                }

                try:
                    # The request is made from the langflow container to itself, so we use the service name
                    response = requests.post(agent_api_url, json=payload, timeout=120)
                    response.raise_for_status()
                    
                    agent_response_data = response.json()
                    # This path is specific to LangFlow's API response structure
                    message_content = agent_response_data.get("outputs", [{}]).get("outputs", [{}]).get("artifacts", {}).get("text", "No text artifact found.")

                    aggregated_results.append({
                        "department": department,
                        "status": "success",
                        "response": message_content
                    })

                except requests.exceptions.RequestException as e:
                    aggregated_results.append({
                        "department": department,
                        "status": "error",
                        "response": f"API call failed: {str(e)}"
                    })

            return {
                "summary_for_user": summary_for_user,
                "aggregated_results": aggregated_results
            }

        except json.JSONDecodeError:
            return {"error": "Invalid JSON from PM agent."}
        except Exception as e:
            return {"error": f"An unexpected error occurred in the orchestrator: {str(e)}"}
