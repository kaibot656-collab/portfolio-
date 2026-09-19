package org.bukkit.event.player;
import org.bukkit.entity.Player;
import org.bukkit.entity.Location;
import org.bukkit.event.Event;
public class PlayerTeleportEvent extends Event {
    private Player player;
    private Location from, to;
    public PlayerTeleportEvent(Player p, Location f, Location t) { this.player = p; this.from = f; this.to = t; }
    public Player getPlayer() { return player; }
    public Location getFrom() { return from; }
    public Location getTo() { return to; }
}