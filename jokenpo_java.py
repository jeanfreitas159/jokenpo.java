import java.util.Random;
import java.util.Scanner;
public class jokenpo_java {
	
	public static void menu(){
		System.out.print("##--Olá Seja Bem vindo ao jogo JoKenpo ninja --##\n\n");        
		System.out.println("##--Por favor digite seu nome --##\n\n");

		Scanner op1 = new Scanner (System.in);
	    String palavra = op1.nextLine();

		System.out.print(palavra);
		System.out.print(" , Digite sua opção de jogo --##\n\n");
        
			System.out.print("-----------------------------\n");
		    System.out.print(" [ 1 ] jogador1   x jogador2 \n");
			System.out.print(" [ 2 ] computador x jogador \n");
			System.out.print(" [ 3 ] Opção Sair              \n");
			System.out.print("-----------------------------\n");	        
			
			Scanner entrada = new Scanner(System.in);

		}

		   public static void jogador(){
		        System.out.println("jogador1 x jogador2.");
		        
		        
		        
		    }

		    public static void pc(){
		        System.out.println("computador x jogador.");}
		   
		        

		    public static void sair(){
		        System.out.println("encerrando jogo.");
		         }

		  
	    public static void main(String[] args) {
	        int opcao;
	        Scanner entrada = new Scanner(System.in);

	        do{
	            menu();
	            opcao = entrada.nextInt();

	            switch(opcao){
	            case 1:
	                jogador();
	                
	                Scanner sc = new Scanner(System.in);
	   			 Scanner sc1 = new Scanner(System.in);

	   				int jogador1,jogador2;
	   				
	   				System.out.println("Escolha sua jogada: ");
	   				System.out.println("Papel = 0 ");
	   				System.out.println("Pedra = 1  ");
	   				System.out.println("Tesoura = 2");
	   				
	   				System.out.println("Jogador 1 digite sua jogada : ");
	   		   		jogador1 = sc.nextInt();
	   				 

	   			    System.out.println("Jogador 2 digite sua jogada : ");
	   				jogador2 = sc1.nextInt();
	   							       		   		
	   		   		 
	   		   		 
	   		   		switch (jogador1) {
	   		   		 case 0 :
	   		   		   System.out.println("jogador1 escolheu papel");
	   		   		    break;
	   		   		 
	   		   		 
	   			     case 1 :
	   		   		   System.out.println("jogador1 escolheu pedra");
	   		   		    break;
	   		   		 
	   		   		 
	   			 case 2 :
	   		   		   System.out.println("jogador1 escolheu tesoura");
	   		   		    break;
	   		   		 }
	   		   		
	   		   		switch (jogador2){
	   		   		 case 0 :
	   		   		   System.out.println("jogador2 escolheu papel");
	   		   		    break;
	   		   		 
	   		   		 
	   			     case 1 :
	   		   		   System.out.println("jogador2 escolheu pedra");
	   		   		    break;
	   		   		 
	   		   		 
	   			 case 2 :
	   		   		   System.out.println("jogador2 escolheu tesoura");
	   		   		    break;
	   		   		 }
	   		   		 
	   		   		 
	   		   	 if ((jogador1 - jogador2)== 0 ) {
	                    System.out.println("Empate .");
		   		  }
	   		   		 
	   		   		 
	   		   	 else  if ((jogador1 - jogador2)== - 1 ) {
	   	                    System.out.println("jogador1 Vencedor .");
	   		   		  }
	   		   			 
	   		   		
	   		   		  else if ((jogador1 - jogador2)==  2) {
	   		   			 System.out.println("jogador1 Vencedor .");}
	   		   			 
	                       
	                       else {
	                       	System.out.println("jogador2 Vencedor .");
	                       }
	                   	
	                break;

	            case 2:
	                pc();
	                {Scanner leitor = new Scanner (System.in);

		            Random gerador = new Random();
		   		
		   		    int usuario ; 
		   		    int computador;
		   		    System.out.println("[ 0 ]Papel  ");
		 		    System.out.println("[ 1 ] Pedra  ");
		 		    System.out.println("[ 2 ]Tesoura");
		 		   
		 		    System.out.println("Digite sua jogada");
			   		  usuario = leitor.nextInt();
		   		    
			   		  computador = gerador.nextInt(3);
		       
		   		 
		   		
	              switch (computador){
		   		 case 0 :
		   		   System.out.println("Computador escolheu papel");
		   		    break;
		   		 
		   		 
			     case 1:
		   		   System.out.println("Computador escolheu pedra");
		   		    break;
		   		 
		   		 
			 case 2 :
		   		   System.out.println("Computador escolheu tesoura");
		   		    break;
		   		 }
		   		 
		   		switch (usuario) {
		   		 case 0 :
		   		   System.out.println("Usuario escolheu papel");
		   		    break;
		   		 
		   		 
			     case 1:
		   		   System.out.println("Usuario escolheu pedra");
		   		    break;
		   		 
		   		 
			 case 2 :
		   		   System.out.println("Usuario escolheu tesoura");
		   		    break;}
		   	   
		   		if ((usuario - computador)== 0 ) {
                    System.out.println("Empate .");
	   		  }
   		   		 
   		   		 
   		   	 else  if ((usuario - computador)== - 1 ) {
   	                    System.out.println("Usuario Vencedor .");
   		   		  }
   		   			 
   		   		
   		   		  else if ((usuario - computador)==  2) {
   		   			 System.out.println("Usuario Vencedor .");}
   		   			 
                       
                       else {
                       	System.out.println("Computador Vencedor .");
                       }
	                }
	   		     case 3:
	                sair();
	                break;

	            default:
	                System.out.println("Opção inválida.");
	            }
	        } while(opcao >3);
	    }
	
	}


