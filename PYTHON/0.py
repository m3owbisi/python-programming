def fifo(pages, frame_size):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        print(f"Frames: {frames}")

    return page_faults

pages = [9, 0, 1, 7, 0, 3, 0, 8, 2, 3, 0]
frame_size = 3
print(f"FIFO Page Faults: {fifo(pages, frame_size)}")