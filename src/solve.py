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
        
def construct_path(paths: dict[str, dict[str, int | list[str]]], goal: str):
    path = [goal]
    while paths[path[-1]]["parents"]:
        path.append(paths[path[-1]]["parents"][0])
    return path

def main(start:str, goal:str): 
    shortest_paths = {start: {"length":0, "parents": None, "visited" : False}}
    while(goal not in shortest_paths):
        # print(shortest_paths)
        shortest_paths = bfs(shortest_paths, goal)
    
    return construct_path(shortest_paths, goal)

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

    args = parser.parse_args()

    start = args.start
    end = args.end

    print(f"start={start}, end={end}")
    print(main(start, end))
