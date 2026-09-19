package org.bukkit.event.player;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;
public class PlayerChatEvent extends Event {
    private Player player;
    private String message;
    public PlayerChatEvent(Player player, String message) { this.player = player; this.message = message; }
    public Player getPlayer() { return player; }
    public String getMessage() { return message; }
    public void setMessage(String msg) { this.message = msg; }
    public void setCancelled(boolean c) {}
    public boolean isCancelled() { return false; }
    public void setFormat(String f) {}
    public String getFormat() { return null; }
}