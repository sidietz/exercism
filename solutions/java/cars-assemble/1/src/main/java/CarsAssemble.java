public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int baseSpeed = 221;
        return switch (speed) {
            case 0 -> 0;
            case 1, 2, 3, 4 -> baseSpeed * speed;
            case 5, 6, 7, 8 -> baseSpeed * speed * 0.9;
            case 9 -> baseSpeed * speed * 0.8;
            case 10 -> baseSpeed * speed * 0.77;
            default -> 0;
        };
    }

    public int workingItemsPerMinute(int speed) {
        return (int) (productionRatePerHour(speed) / 60.0);
    }
}
