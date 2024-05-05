from utils import read_video, save_video

def main():
    #Read video
    video_frame = read_video('input_videos/08fd33_4.mp4')
    
    #Save Video
    save_video(video_frame, 'output_videos/op_vdo.avi')

if __name__ == '__main__':
    main()
    