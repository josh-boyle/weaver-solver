import words
def bfs(paths: dict[str, dict[str, int | list[str]]], goal: str):
    new_paths = paths.copy()
    for path in paths:
        if paths[path]["visited"]:
            continue
        paths[path]["visited"] = True
        for neighbor in words.get_words_one_letter_off(path):
            if neighbor not in new_paths:
                # print("path", path,"to", neighbor)
                new_paths[neighbor] = {"length": paths[path]["length"] + 1, "parents": [path], "visited": False}
    # print(new_paths)
    return new_paths

def bidir_bfs(top: dict[str, dict[str, int | list[str]]],bottom: dict[str, dict[str, int | list[str]]]):
    if len(top) <= len(bottom):
        expanding = top
        other = bottom
        expanding_is_top = True
    else:
        expanding = bottom
        other = top
        expanding_is_top = False
    
    new_paths = expanding.copy()
    for word,meta in expanding.items():
        if meta["visited"]:
            continue

        meta["visited"] = True

        for neighbor in words.get_words_one_letter_off(word):
            if neighbor not in new_paths:
                new_paths[neighbor] = {"length": expanding[word]["length"] + 1, "parents": [word], "visited": False}
                if neighbor in other:
                    return (neighbor, new_paths, other) if expanding_is_top else (neighbor, other, new_paths)

    return (None, new_paths, other) if expanding_is_top else (None, other, new_paths )

def construct_path(paths: dict[str, dict[str, int | list[str]]], goal: str, is_forward: bool):
    path = [goal]
    while paths[path[-1]]["parents"]:
        path.append(paths[path[-1]]["parents"][0])
    if is_forward:
        path = path[::-1]
    return path

def construct_path_bidir(start_paths: dict[str, dict[str, int | list[str]]],end_paths: dict[str, dict[str, int | list[str]]], intersect: str):
    start = construct_path(start_paths,intersect, True)
    end = construct_path(end_paths,intersect, False)
    return start + end[1:]

def main(start:str, end:str, bidir: bool): 
    start_paths = {start: {"length":0, "parents": None, "visited" : False}}
    if bidir:
        end_paths = {end: {"length":0, "parents": None, "visited" : False}}
        intersect = None
        while not intersect:
            intersect, start_paths, end_paths = bidir_bfs(start_paths,end_paths)
        return construct_path_bidir(start_paths, end_paths, intersect)
    else:
        while(end not in start_paths):
            start_paths = bfs(start_paths, end)
        return construct_path(start_paths, end, True)
    

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process start and end."
    )

    parser.add_argument(
        "-s", "--start",
        type=str,
        default="love",
        help='Start value (default: "love")'
    )

    parser.add_argument(
        "-e", "--end",
        type=str,
        default="hate",
        help='End value (default: "hate")'
    )

    parser.add_argument(
        "-b", "--bidir",
        action="store_true",
        help="Use bidirectional BFS"
    )

    args = parser.parse_args()

    start = args.start
    end = args.end
    bidir = args.bidir
    mode = "bidirectional BFS" if bidir else "BFS"

    print(f"start={start}, end={end}: Using {mode}")
    print(main(start, end, bidir))
