import javafx.animation.PauseTransition;
import javafx.application.Application;
import javafx.application.Platform;

import java.io.*;
import java.util.Timer;
import java.util.TimerTask;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextInputDialog;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.util.*;

public class a extends Application {
    int score=0;
    int mathces=0;
    int misses=0;
    int timeLeft = 60;
    public static void main(String[] args) {
        launch();
    }
    @Override
    public void start(Stage primaryStage) throws Exception { game(); }
    public void game(){
        reset();
        Stage window = new Stage();
        AnchorPane MPane = new AnchorPane();
        Scene MScene = new Scene(MPane, 900,600 );
        //MScene.getStylesheets().add("style.css");
        window.setTitle("mach game");
        window.setScene(MScene);
        window.show();

        Label Score = new Label();
        Score.setText("Score");
        Score.setFont(new Font("Arial", 45));
        MPane.getChildren().add(Score);
        AnchorPane.setRightAnchor(Score,70d);
        AnchorPane.setTopAnchor(Score,10d);

        Label Scorev = new Label();
        Scorev.setText(String.valueOf(score));
        Scorev.setFont(new Font("Arial", 45));
        MPane.getChildren().add(Scorev);
        AnchorPane.setRightAnchor(Scorev,10d);
        AnchorPane.setTopAnchor(Scorev,10d);

        Label timerL = new Label();
        timerL.setText(String.valueOf(timeLeft));
        timerL.setFont(new Font("Arial", 45));
        MPane.getChildren().add(timerL);
        AnchorPane.setRightAnchor(timerL,10d);
        AnchorPane.setTopAnchor(timerL,50d);

        Label timerLc = new Label();
        timerLc.setText("Time");
        timerLc.setFont(new Font("Arial", 45));
        MPane.getChildren().add(timerLc);
        AnchorPane.setRightAnchor(timerLc,83d);
        AnchorPane.setTopAnchor(timerLc,50d);

        Timer timer = new Timer();
        TimerTask task = new TimerTask(){
            public void run(){
                if(timeLeft<=0) {
                    timer.cancel();
                    Platform.runLater(() ->{
                        window.close();
                        timer.cancel();
                        //task.cancel();
                        lost();
                    });
                }else{
                    timeLeft--;
                    System.out.println(timeLeft);
                    Platform.runLater(() -> timerL.setText(String.valueOf(timeLeft)));
                }
            }
        };

        timer.schedule(task, 0, 1000 );
        GridPane first = new GridPane();
        first.setPadding(new Insets(2, 2, 2, 2));
        first.setHgap(10);
        first.setVgap(10);

        Image square = new Image(getClass().getResourceAsStream
                ("/square.png"));
        Image triangle = new Image(getClass().getResourceAsStream
                ("/trangle.png"));
        Image cover = new Image(getClass().getResourceAsStream
                ("/cover.png"));
        Image Hexagon = new Image(getClass().getResourceAsStream
                ("/Hexagon.png"));


        ArrayList<Image> iconlist = new ArrayList<>();
        ArrayList<Image> temp = new ArrayList<>();
        ArrayList<ImageView> tempc = new ArrayList<>();

        int number=0;

        for (int i=0;i<4;i++){
            iconlist.add(triangle);
            iconlist.add(square);
            iconlist.add(Hexagon);
        }
        Collections.shuffle(iconlist);

        for (int r = 1; r < 4; r++) {
            for (int c = 1; c < 5; c++) {
                if (number <12)
                {
                    ImageView bottom = new ImageView(iconlist.get(number));
                    bottom.setId(String.valueOf(number));
                    ImageView top = new ImageView(cover);
                    top.setId(String.valueOf(number));
                    first.add(bottom, c, r);
                    first.add(top, c, r);
                    top.setOnMouseClicked(event -> {
                        if (temp.size()<2) {
                            top.setImage(null);
                            temp.add(bottom.getImage());
                            tempc.add(top);
                            System.out.println(temp);
                        }

                        if(temp.size()==2){
                            if(temp.get(0)==temp.get(1)){
                                score+=2;
                                mathces+=1;
                                Scorev.setText(String.valueOf(score));
                                temp.clear();
                                tempc.clear();
                                if (mathces==6) {
                                    timer.cancel();
                                    won();
                                    window.close();

                                }
                            }else {
                                PauseTransition pause = new PauseTransition(Duration.millis(200));
                                pause.setOnFinished(event2 ->{
                                    misses+=1;
                                    tempc.get(0).setImage(cover);
                                    tempc.get(1).setImage(cover);
                                    temp.clear();
                                    tempc.clear();
                                });
                                pause.play();
                            }
                        }
                    });
                    number++;
                }
            }
        }
        MPane.getChildren().add(first);
        AnchorPane.setTopAnchor(first,98d);
        AnchorPane.setLeftAnchor(first,70d);
    }
    private void lost() {
        Stage windowL = new Stage();
        AnchorPane LPane = new AnchorPane();
        Scene LScene = new Scene(LPane, 900,600 );
        //LScene.getStylesheets().add("style.css");
        windowL.setTitle("You Lost");
        windowL.setScene(LScene);
        windowL.show();

        Label labelL = new Label();
        labelL.setText("You LOST");
        labelL.setFont(new Font("Arial", 45));
        labelL.setStyle("-fx-background-color: #ffbebe; ");
        LPane.getChildren().add(labelL);
        AnchorPane.setLeftAnchor(labelL,370d);
        AnchorPane.setTopAnchor(labelL,200d);

        Label labelS = new Label();
        labelS.setText("Score: "+score);
        labelS.setFont(new Font("Arial", 45));
        labelS.setStyle("-fx-background-color: #ffbebe; ");
        LPane.getChildren().add(labelS);
        AnchorPane.setLeftAnchor(labelS,260d);
        AnchorPane.setTopAnchor(labelS,260d);

        Label labelT = new Label();
        labelT.setText("Time: "+timeLeft);
        labelT.setFont(new Font("Arial", 45));
        labelT.setStyle("-fx-background-color: #ffbebe; ");
        LPane.getChildren().add(labelT);
        AnchorPane.setLeftAnchor(labelT,480d);
        AnchorPane.setTopAnchor(labelT,260d);

        Button quitbutton = new Button("QUIT");
        quitbutton.setMinSize(100, 60);
        quitbutton.setStyle("-fx-background-color: #d21e3c; ");
        quitbutton.setOnMouseEntered(event ->  quitbutton.setStyle("-fx-background-color: #c64058; "));
        quitbutton.setOnMouseExited(event ->  quitbutton.setStyle("-fx-background-color: #d21e3c; "));
        quitbutton.setOnAction(event -> {
            System.exit(0);
        });
        LPane.getChildren().add(quitbutton);
        AnchorPane.setBottomAnchor(quitbutton,200d);
        AnchorPane.setLeftAnchor(quitbutton,500d);

        Button retrybutton = new Button("REPLAY");
        retrybutton.setMinSize(100, 60);
        retrybutton.setStyle("-fx-background-color: #d21e3c; ");
        retrybutton.setOnMouseEntered(event ->  retrybutton.setStyle("-fx-background-color: #c64058; "));
        retrybutton.setOnMouseExited(event ->  retrybutton.setStyle("-fx-background-color: #d21e3c; "));
        retrybutton.setOnAction(event -> {
            windowL.close();
            reset();
            game();
        });
        LPane.getChildren().add(retrybutton);
        AnchorPane.setBottomAnchor(retrybutton,200d);
        AnchorPane.setLeftAnchor(retrybutton,200d);
    }
    private void won(){
        Stage windowW = new Stage();
        AnchorPane WPane = new AnchorPane();
        Scene WScene = new Scene(WPane, 900,600 );
        //WScene.getStylesheets().add("/style.css");
        windowW.setTitle("You Won");
        windowW.setScene(WScene);
        WPane.setStyle("-fx-background-color: #03560f;");
        windowW.show();

        Label labelW = new Label();
        labelW.setText("You WON");
        labelW.setFont(new Font("Arial", 45));
        labelW.setStyle("-fx-background-color: #beffbe; ");
        WPane.getChildren().add(labelW);
        AnchorPane.setLeftAnchor(labelW,370d);
        AnchorPane.setTopAnchor(labelW,200d);

        Label labelS = new Label();
        labelS.setText("Score: "+score);
        labelS.setFont(new Font("Arial", 45));
        labelS.setStyle("-fx-background-color: #beffbe; ");
        WPane.getChildren().add(labelS);
        AnchorPane.setLeftAnchor(labelS,260d);
        AnchorPane.setTopAnchor(labelS,260d);

        Label labelT = new Label();
        labelT.setText("Time: "+timeLeft);
        labelT.setFont(new Font("Arial", 45));
        labelT.setStyle("-fx-background-color: #beffbe; ");
        WPane.getChildren().add(labelT);
        AnchorPane.setLeftAnchor(labelT,480d);
        AnchorPane.setTopAnchor(labelT,260d);

        Button quitbutton = new Button("QUIT");
        quitbutton.setMinSize(100, 60);
        quitbutton.setStyle("-fx-background-color: #d21e3c; ");
        quitbutton.setOnMouseEntered(event ->  quitbutton.setStyle("-fx-background-color: #c64058; "));
        quitbutton.setOnMouseExited(event ->  quitbutton.setStyle("-fx-background-color: #d21e3c; "));
        quitbutton.setOnAction(event -> {
            System.exit(0);
        });
        WPane.getChildren().add(quitbutton);
        AnchorPane.setBottomAnchor(quitbutton,200d);
        AnchorPane.setLeftAnchor(quitbutton,500d);

        Button retrybutton = new Button("REPLAY");
        retrybutton.setMinSize(100, 60);
        retrybutton.setStyle("-fx-background-color: #d21e3c; ");
        retrybutton.setOnMouseEntered(event ->  retrybutton.setStyle("-fx-background-color: #c64058; "));
        retrybutton.setOnMouseExited(event ->  retrybutton.setStyle("-fx-background-color: #d21e3c; "));
        retrybutton.setOnAction(event -> {
            windowW.close();
            reset();
            game();
        });
        WPane.getChildren().add(retrybutton);
        AnchorPane.setBottomAnchor(retrybutton,200d);
        AnchorPane.setLeftAnchor(retrybutton,200d);

        TextInputDialog dialog = new TextInputDialog("USERNAME");
        dialog.setTitle("Leaderboard");
        Optional<String> result = dialog.showAndWait();
        dialog.setHeaderText("Join the Leaderboard");
        dialog.setContentText("Please enter your name:");
        saveleaderboad(dialog.getResult());
    }
    private void saveleaderboad(String name){
        File file = new File("C:/Users/uwiN viDamage/IdeaProjects/convert tile match Py to java/src/save.txt");
        FileWriter fw = null;
        try {
            fw = new FileWriter(file,true);
        } catch (IOException e) {
            e.printStackTrace();
        }
        BufferedWriter bw = new BufferedWriter(fw);
        try {
            bw.write(name+":"+score+":"+timeLeft);
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void showleaderboad(){
        Scanner scanSeats = null;
        try {
            scanSeats = new Scanner(new File("seats.txt"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while(scanSeats.hasNext()) {
            System.out.println(scanSeats.next());
        }
    }
    private void reset(){
        score=0;
        mathces=0;
        misses=0;
        timeLeft = 60;
    }
}