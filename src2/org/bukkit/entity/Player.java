package org.bukkit.entity;
import java.util.UUID;
import org.bukkit.command.CommandSender;
public class Player extends CommandSender {
    public String getName() { return "Player"; }
    public void sendMessage(String msg) {}
    public void teleport(Location loc) {}
    public Location getLocation() { return new Location(null, 0, 0, 0); }
    public UUID getUniqueId() { return null; }
    public boolean isOnline() { return true; }
    public void setPlayerListName(String name) {}
}