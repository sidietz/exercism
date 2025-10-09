class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {

    @Override
    boolean isVulnerable() {
        return false;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable() ? 10 : 6;
    }

    @Override
    public String toString() {
        return "Fighter is a Warrior";
    }
}

class Wizard extends Fighter {

    boolean vulnerable = true;

    @Override
    boolean isVulnerable() {
        return this.vulnerable;
    }

    void prepareSpell() {
        this.vulnerable = false;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return !this.vulnerable ? 12 : 3;
    }

    @Override
    public String toString() {
        return "Fighter is a Wizard";
    }
}