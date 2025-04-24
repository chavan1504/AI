class TowerOfHanoi:
    def __init__(self, n):
        self.n = n
        self.rods = {'Rod 1': list(range(n, 0, -1)), 'Rod 2': [], 'Rod 3': []}
    
    def goal_state(self):
        return {'Rod 1': [], 'Rod 2': [], 'Rod 3': list(range(self.n, 0, -1))}
    
    def legal_move(self, src, dest):
        return self.rods[src] and (not self.rods[dest] or self.rods[src][-1] < self.rods[dest][-1])
    
    def move_disk(self, src, dest):
        if self.legal_move(src, dest):
            disk = self.rods[src].pop()
            self.rods[dest].append(disk)
            print(f"Move disk {disk} from {src} to {dest}")
        
    def solve(self, n, src, aux, dest):
        if n == 1:
            self.move_disk(src, dest)
        else:
            self.solve(n-1, src, dest, aux)
            self.move_disk(src, dest)
            self.solve(n-1, aux, src, dest)

# Run the problem
n = 3
hanoi = TowerOfHanoi(n)
print("Initial state:", hanoi.rods)
print("Goal state:", hanoi.goal_state())
print("\nSolution steps:")
hanoi.solve(n, 'Rod 1', 'Rod 2', 'Rod 3')
print("\nFinal state:", hanoi.rods)
