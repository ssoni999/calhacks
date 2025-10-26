#!/usr/bin/env python3
"""
Standalone script to run AI scoring on candidates
Usage: python run_ai_scoring.py

This script automatically loads job descriptions and rubrics from:
- job_descriptions/ folder
- rubrics/ folder

It scores all candidates based on their position.
"""

from ai_scorer import score_all_candidates_auto
import json

def main():
    print("🤖 Starting AI-powered candidate scoring...")
    print("📁 Loading job descriptions and rubrics from files...")
    print("=" * 60)
    
    # Score all candidates automatically
    results = score_all_candidates_auto()
    
    print("\n" + "=" * 60)
    print("✨ AI scoring complete!")
    print(f"📊 Scored candidates for {results['total_positions']} positions")
    print("💾 All scores saved to database")
    print("=" * 60)
    
    # Print summary
    for position_result in results['positions']:
        print(f"\n{position_result['position']}: {position_result['total_candidates']} candidates scored")

if __name__ == "__main__":
    main()
