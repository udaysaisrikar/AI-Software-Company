import os
from rich.console import Console
from datetime import datetime

console = Console()

def generate_report(response):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/idea_report_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response)
    
    console.print(f"[bold green]✓ Report saved:[/] {filename}")
    