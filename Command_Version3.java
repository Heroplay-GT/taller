import java.util.ArrayList;
import java.util.List;

// Command interface
interface Command {
    void execute();
    void undo();
}

// Receiver
class Light {
    private boolean isOn = false;
    
    public void turnOn() {
        isOn = true;
        System.out.println("Light is ON");
    }
    
    public void turnOff() {
        isOn = false;
        System.out.println("Light is OFF");
    }
    
    public boolean isOn() {
        return isOn;
    }
}

class Fan {
    private int speed = 0; // 0=off, 1=low, 2=medium, 3=high
    
    public void setSpeed(int speed) {
        this.speed = speed;
        String[] speeds = {"OFF", "LOW", "MEDIUM", "HIGH"};
        System.out.println("Fan speed set to: " + speeds[speed]);
    }
    
    public int getSpeed() {
        return speed;
    }
}

// Concrete commands
class LightOnCommand implements Command {
    private Light light;
    
    public LightOnCommand(Light light) {
        this.light = light;
    }
    
    @Override
    public void execute() {
        light.turnOn();
    }
    
    @Override
    public void undo() {
        light.turnOff();
    }
}

class LightOffCommand implements Command {
    private Light light;
    
    public LightOffCommand(Light light) {
        this.light = light;
    }
    
    @Override
    public void execute() {
        light.turnOff();
    }
    
    @Override
    public void undo() {
        light.turnOn();
    }
}

class FanSpeedCommand implements Command {
    private Fan fan;
    private int speed;
    private int previousSpeed;
    
    public FanSpeedCommand(Fan fan, int speed) {
        this.fan = fan;
        this.speed = speed;
    }
    
    @Override
    public void execute() {
        previousSpeed = fan.getSpeed();
        fan.setSpeed(speed);
    }
    
    @Override
    public void undo() {
        fan.setSpeed(previousSpeed);
    }
}

// Null Object pattern for commands
class NoCommand implements Command {
    @Override
    public void execute() {}
    
    @Override
    public void undo() {}
}

// Invoker
class RemoteControl {
    private Command[] onCommands;
    private Command[] offCommands;
    private Command undoCommand;
    
    public RemoteControl() {
        onCommands = new Command[7];
        offCommands = new Command[7];
        
        Command noCommand = new NoCommand();
        for (int i = 0; i < 7; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
        undoCommand = noCommand;
    }
    
    public void setCommand(int slot, Command onCommand, Command offCommand) {
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;
    }
    
    public void onButtonPressed(int slot) {
        onCommands[slot].execute();
        undoCommand = onCommands[slot];
    }
    
    public void offButtonPressed(int slot) {
        offCommands[slot].execute();
        undoCommand = offCommands[slot];
    }
    
    public void undoButtonPressed() {
        undoCommand.undo();
    }
}

// Cliente
public class Command {
    public static void main(String[] args) {
        // Crear receivers
        Light livingRoomLight = new Light();
        Fan ceilingFan = new Fan();
        
        // Crear commands
        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
        FanSpeedCommand fanMedium = new FanSpeedCommand(ceilingFan, 2);
        FanSpeedCommand fanOff = new FanSpeedCommand(ceilingFan, 0);
        
        // Crear invoker
        RemoteControl remote = new RemoteControl();
        
        // Configurar commands
        remote.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remote.setCommand(1, fanMedium, fanOff);
        
        // Usar remote
        System.out.println("=== Testing Light ===");
        remote.onButtonPressed(0);
        remote.offButtonPressed(0);
        remote.undoButtonPressed();
        
        System.out.println("\n=== Testing Fan ===");
        remote.onButtonPressed(1);
        remote.offButtonPressed(1);
        remote.undoButtonPressed();
    }
}