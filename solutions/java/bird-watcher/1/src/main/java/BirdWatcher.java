
class BirdWatcher {
    private final int[] birdsPerDay;
    private static final int BUSY_COUNT = 5;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return birdsPerDay.clone();
    }

    public int getToday() {
        return birdsPerDay[birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        int currentCount = birdsPerDay[birdsPerDay.length - 1];
        birdsPerDay[birdsPerDay.length - 1] = currentCount + 1;
        return;
    }

    public boolean hasDayWithoutBirds() {
        boolean daysWithoutBirds = false;
        for (int i : birdsPerDay) {
            daysWithoutBirds = daysWithoutBirds || (i == 0);
        }
        return daysWithoutBirds;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        int minVal = Math.min(numberOfDays, birdsPerDay.length);
        for (int i = 0; i < minVal; i++) {
            count = count + birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int count = 0;
        for (int i = 0; i < birdsPerDay.length; i++) {
            if (birdsPerDay[i] >= BUSY_COUNT) {
                count = count + 1;
            }
        }
        return count;
    }
}
