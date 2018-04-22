import java.awt.*;
import java.awt.event.*;

public class Block extends Frame {
    private int fps = 30;

    private static final int GAME_WIDTH = 600;
    private static final int GAME_HEIGHT = 400;

    private int x = 50;

    private Image offScreenImage = null;

    public void paint(Graphics g) {
        g.setColor(Color.BLUE);
        g.fillRect(x, 380, 60, 30);
    }

    public void update(Graphics g) {
        if (offScreenImage == null) {
            offScreenImage = this.createImage(GAME_WIDTH, GAME_HEIGHT);
        }
        Graphics gOffScreen = offScreenImage.getGraphics();
        gOffScreen.setColor(Color.WHITE);
        gOffScreen.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

        paint(gOffScreen);
        g.drawImage(offScreenImage, 0, 0, null);
    }

    private void launchFrame() {
        this.setLocation(100, 100);
        this.setSize(GAME_WIDTH, GAME_HEIGHT);
        this.setTitle("block");
        this.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
        this.setResizable(false);
        this.addKeyListener(new KeyMonitor());
        this.setVisible(true);

        new Thread(new PaintThread()).start();
    }


    private class PaintThread implements Runnable {

        public void run() {
            for (; ; ) {
                repaint();
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private class KeyMonitor extends KeyAdapter {

        private int offset = fps;

        public void keyPressed(KeyEvent e) {
            int key = e.getKeyCode();
            switch (key) {
                case KeyEvent.VK_LEFT:
                    x -= offset;
                    break;
                case KeyEvent.VK_RIGHT:
                    x += offset;
                    break;
            }
        }

    }

    public static void main(String[] args) {
        Block tc = new Block();
        tc.launchFrame();
    }
}
