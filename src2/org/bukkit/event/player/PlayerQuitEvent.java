package org.bukkit.event.player;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;
public class PlayerQuitEvent extends Event {
    private Player player;
    public PlayerQuitEvent(Player player) { this.player = player; }
    public Player getPlayer() { return player; }
}