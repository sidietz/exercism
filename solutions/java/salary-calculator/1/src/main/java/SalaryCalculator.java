public class SalaryCalculator {

    private static final int BASE_SALARAY = 1000;
    
    public double salaryMultiplier(int daysSkipped) {
        return daysSkipped >= 5 ? 0.85 : 1.0;
    }

    public int bonusMultiplier(int productsSold) {
        return productsSold >= 20 ? 13 : 10;
    }

    public double bonusForProductsSold(int productsSold) {
        return productsSold * bonusMultiplier(productsSold);
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        return Math.min(2000.0, salaryMultiplier(daysSkipped) * BASE_SALARAY + bonusForProductsSold(productsSold));
    } 
}
