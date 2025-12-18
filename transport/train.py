class Train(Vehicle):
    def __init__(self, capacity: float, number_of_cars: int):
        super().__init__(capacity)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return (f"Train ({self.number_of_cars} cars) | ID: {self.vehicle_id} | "
                f"Capacity: {self.capacity}t | Load: {self.current_load}t")