package org.bukkit.command;
public class Command {
    private String name;
    public Command(String name) { this.name = name; }
    public String getName() { return name; }
    public boolean execute(CommandSender sender, String label, String[] args) { return false; }
}