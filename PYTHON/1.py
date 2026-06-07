#Python program for Optimal page replacement algorithm.
def optimal(pages, frame_size):
    frames = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the page that will not be used for the longest time
                future_uses = []
                for frame in frames:
                    if frame in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(frame))
                    else:
                        future_uses.append(float('inf'))
                # Replace the page with the highest index (or inf)
                frames.pop(future_uses.index(max(future_uses)))
                frames.append(page)
            page_faults += 1
        print(f"Frames: {frames}")

    return page_faults

pages = [9, 0, 1, 7, 0, 3, 0, 8, 2, 3, 0]
frame_size = 3
print(f"Optimal Page Faults: {optimal(pages, frame_size)}")