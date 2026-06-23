class Badge {
    public String print(Integer id, String name, String department) {
        String safeDepartment = department == null ? "OWNER" : department.toUpperCase();
        String tails = String.format("%s - %s", name, safeDepartment);
        return id == null ? tails : String.format("[%d] - %s", id, tails);
    }
}
