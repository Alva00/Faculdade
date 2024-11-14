def distance_to_be_covered_user():
    while True:
        distance_to_be_covered = input("Insira a distância a ser percorrida, em km (ex.: 10,5).\nkm ").replace(",", ".")
        try:
            distance_to_be_covered = float(distance_to_be_covered)
        except ValueError:
            print("Insira um valor válido (ex.: 10 | 10,5).")
            return
        if distance_to_be_covered <= 0:
            print("Insira um valor positivo.")
            continue
        break
    distance_traveled_user(distance_to_be_covered)
    
def distance_traveled_user(distance_to_be_covered):
    current_distance = 0
    intervals_covered = 0
    interval_length = 1
    
    while current_distance < distance_to_be_covered:
        print(f"Distância atual percorrida: {current_distance} km. Meta final: {distance_to_be_covered} km.")
        if (current_distance + interval_length) < distance_to_be_covered:
            input(f"Insira algo quando completar {interval_length:.2f} quilômetro(s).\n")    
        else:
            input(f"Insira algo quando completar {(distance_to_be_covered - current_distance):.2f} quilômetro(s).\n")
        
        intervals_covered += 1
        current_distance = round(intervals_covered*interval_length, 2)
        
    print(f"Trajeto finalizado! Você percorreu {distance_to_be_covered} km em {intervals_covered} intervalos.")

def main():
    distance_to_be_covered_user()
       
if __name__ == "__main__":
    main()