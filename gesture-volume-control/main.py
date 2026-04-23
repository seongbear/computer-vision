from app.volume_control import run_volume_control

def main():
    print("--- Gesture Volume Control Started ---")
    print("Camera activating... bring your thumb and index finger into the frame.")
    print("Press 'q' in the video window to quit.")
    
    try:
        run_volume_control()
    except KeyboardInterrupt:
        print("\nForce closed by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()