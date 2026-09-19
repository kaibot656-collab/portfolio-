package org.bukkit.event.player;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;
public class PlayerCommandPreprocessEvent extends Event {
    private Player player;
    private String message;
    public PlayerCommandPreprocessEvent(Player p, String m) { this.player = p; this.message = m; }
    public Player getPlayer() { return player; }
    public String getMessage() { return message; }
    public void setCancelled(boolean c) {}
    public boolean isCancelled() { return false; }
}