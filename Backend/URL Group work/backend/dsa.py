# ==============================
# 1. HASH TABLE (WITH COLLISION HANDLING)
# ==============================

HASH_SIZE = 10
url_cache = [[] for _ in range(HASH_SIZE)]


def _hash(key):
    return sum(ord(c) for c in key) % HASH_SIZE


def cache_url(short_code, long_url):
    index = _hash(short_code)
    bucket = url_cache[index]

    for item in bucket:
        if item[0] == short_code:
            item[1] = long_url
            return

    # collision handled here (separate chaining)
    bucket.append([short_code, long_url])


def get_cached_url(short_code):
    index = _hash(short_code)
    bucket = url_cache[index]

    for item in bucket:
        if item[0] == short_code:
            return item[1]

    return None


# ==============================
# 2. STACK (UNDO FEATURE)
# ==============================

undo_stack = []

def push_deleted(url_obj):
    undo_stack.append(url_obj)


def pop_restore():
    if undo_stack:
        return undo_stack.pop()
    return None


# ==============================
# 3. QUEUE (REQUEST BUFFERING)
# ==============================

from collections import deque

request_queue = deque()

def add_request(url):
    request_queue.append(url)


def process_request():
    if request_queue:
        return request_queue.popleft()
    return None


# ==============================
# 4. HEAP (TOP CLICKED URLs)
# ==============================

import heapq

click_heap = []

def add_click(short_code, clicks):
    heapq.heappush(click_heap, (-clicks, short_code))


def get_top_clicked():
    return heapq.nsmallest(5, click_heap)


# ==============================
# 5. SORTING (RANKING)
# ==============================

def sort_urls_by_clicks(url_list):
    return sorted(url_list, key=lambda x: x.click_count, reverse=True)


# ==============================
# 6. SEARCHING (BINARY SEARCH)
# ==============================

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ==============================
# 7. GRAPH (SYSTEM FLOW)
# ==============================

system_graph = {
    "Frontend": ["API Server"],
    "API Server": ["Database", "Cache"],
    "Database": [],
    "Cache": []
}


def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(system_graph[node])

    return visited