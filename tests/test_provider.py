import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.job_sources.provider_registry import get_providers


def main():

    providers = get_providers()

    results = []

    print("=" * 70)
    print("AI JOB HUNTER - PROVIDER HEALTH CHECK")
    print("=" * 70)

    for provider in providers:

        start = time.time()

        try:

            jobs = provider.search("", "Bengaluru")

            elapsed = round(time.time() - start, 2)

            results.append({
                "provider": provider.__class__.__name__,
                "jobs": len(jobs),
                "time": elapsed,
                "status": "PASS"
            })

        except Exception as e:

            elapsed = round(time.time() - start, 2)

            results.append({
                "provider": provider.__class__.__name__,
                "jobs": 0,
                "time": elapsed,
                "status": f"FAIL ({e})"
            })

    print("\n")
    print("{:<25} {:<10} {:<10} {}".format(
        "Provider",
        "Jobs",
        "Time",
        "Status"
    ))

    print("-" * 70)

    total = 0

    for r in results:

        total += r["jobs"]

        print("{:<25} {:<10} {:<10} {}".format(
            r["provider"],
            r["jobs"],
            str(r["time"]) + "s",
            r["status"]
        ))

    print("-" * 70)
    print(f"TOTAL JOBS : {total}")


if __name__ == "__main__":
    main()