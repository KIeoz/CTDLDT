def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ {source} -> {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Di chuyển đĩa {n} từ {source} -> {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)
#test
tower_of_hanoi(3, 'A', 'B', 'C')
