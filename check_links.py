import requests
import sys

base_url = "http://127.0.0.1:5000"
routes = [
    "/",
    "/api/material_data",
    "/careers",
    "/thermosolver/",
    "/stressmaster/",
    "/about-us",
    "/product",
    "/mechai",
    "/fluid-flow",
    "/mech-ai/",
    "/fluid_flow_ai/",
    "/security/",
    "/design_master/",
    "/resources/",
    "/manufacturing-twin",
    "/manufactaring_twin/",
    "/robopilot-ai",
    "/robopilot_ai/",
    "/mat-si",
    "/mat_si/",
    "/enginetune/",
    "/mesh-mind/",
    "/demo/",
    "/view_requests"
]

def check_links():
    print(f"Checking {len(routes)} routes on {base_url}...")
    success_count = 0
    for route in routes:
        url = base_url + route
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[OK] {route}")
                success_count += 1
            else:
                print(f"[FAIL] {route} - Status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"[ERROR] Could not connect to {base_url}. Is the server running?")
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR] {route} - {e}")
    
    print(f"\nSummary: {success_count}/{len(routes)} routes working.")

if __name__ == "__main__":
    check_links()
