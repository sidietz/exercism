public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method

    private static final int EXPECTED_MINUTES_IN_OVEN = 40;

    public int expectedMinutesInOven(){
        return EXPECTED_MINUTES_IN_OVEN;
    }

    public int remainingMinutesInOven(int actualMinutes) {
        return expectedMinutesInOven() - actualMinutes;
    }

    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    public int totalTimeInMinutes(int layers, int ovenTime) {
        return preparationTimeInMinutes(layers) + ovenTime;
    }

    // TODO: define the 'remainingMinutesInOven()' method

    // TODO: define the 'preparationTimeInMinutes()' method

    // TODO: define the 'totalTimeInMinutes()' method
}
