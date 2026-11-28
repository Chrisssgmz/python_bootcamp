eggs_list = [1, 2, 3, 4, 5]

def count_dinosaurs_eggs(eggs: list[int]) -> tuple[int, int]:
    """
    Count the number of carnivore and herbivore dinosaur eggs in the list.
    """
    
    total_carnivores: int = 0
    total_herbivores: int = 0
    
    for egg in eggs:
        if egg % 2 == 0:
            total_carnivores += 1
        else:
            total_herbivores += 1
            
    return total_carnivores, total_herbivores

count_carnivores, count_herbivores = count_dinosaurs_eggs(eggs_list)

print(f"Total Carnivores: {count_carnivores}")
print(f"Total Herbivores: {count_herbivores}")