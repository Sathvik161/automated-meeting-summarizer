import os
import subprocess

def run_pipeline(audio_file):
    """
    Run the complete pipeline: transcribe → summarize → extract actions
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    print("Transcribing audio...")
    subprocess.run(["python", "scripts/transcribe.py", audio_file], check=True)
    
    print("\nGenerating summary...")
    subprocess.run(["python", "scripts/summarize.py"], check=True)
    
    print("\nExtracting action items...")
    subprocess.run(["python", "scripts/extract_actions.py"], check=True)
    
    print("\nPipeline completed. Check the outputs/ directory for results.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python pipeline.py <audio_file_path>")
        sys.exit(1)
    
    run_pipeline(sys.argv[1])