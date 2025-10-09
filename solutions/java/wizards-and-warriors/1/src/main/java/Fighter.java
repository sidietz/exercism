class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {

    boolean isVulnerable() {
        return false;
    }

    int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable() ? 10 : 6;
    }

    public String toString() {
        return "Fighter is a Warrior";
    }
}

class Wizard extends Fighter {

    boolean vulnerable = true;

    boolean isVulnerable() {
        return this.vulnerable;
    }

    void prepareSpell() {
        this.vulnerable = false;
    }

    int getDamagePoints(Fighter fighter) {
        return !this.vulnerable ? 12 : 3;
    }

    public String toString() {
        return "Fighter is a Wizard";
    }
}