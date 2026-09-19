package org.bukkit.command;
public class CommandSender {
    public boolean hasPermission(String perm) { return true; }
    public void sendMessage(String msg) {}
    public String getName() { return "Console"; }
    public java.util.UUID getUniqueId() { return null; }
}