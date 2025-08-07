package cours;

	public class NombreReel {
	    // Attributs privés pour l'encapsulation
	    private double valeur;
	    private char etiquette;

	    // Constructeur explicite
	    public NombreReel(double valeur, char etiquette) {
	        this.valeur = valeur;
	        // Vérification que l'étiquette est une lettre minuscule
	        if (etiquette >= 'a' && etiquette <= 'z') {
	            this.etiquette = etiquette;
	        } else {
	            throw new IllegalArgumentException("L'étiquette doit être une lettre minuscule.");
	        }
	    }

	    // Getters et Setters pour l'encapsulation
	    public double getValeur() {
	        return valeur;
	    }

	    public void setValeur(double valeur) {
	        this.valeur = valeur;
	    }

	    public char getEtiquette() {
	        return etiquette;
	    }

	    public void setEtiquette(char etiquette) {
	        if (etiquette >= 'a' && etiquette <= 'z') {
	            this.etiquette = etiquette;
	        } else {
	            throw new IllegalArgumentException("L'étiquette doit être une lettre minuscule.");
	        }
	    }

	    // Méthodes pour les traitements
	    public double valeurAbsolue() {
	        return Math.abs(valeur);
	    }

	    public int signe() {
	        if (valeur > 0) {
	            return 1;
	        } else if (valeur < 0) {
	            return -1;
	        } else {
	            return 0;
	        }
	    }

	    public double oppose() {
	        return -valeur;
	    }

	    public int comparer(NombreReel autre) {
	        return Double.compare(this.valeur, autre.valeur);
	    }

	    @Override
	    public String toString() {
	        return "NombreReel{" +
	                "valeur=" + valeur +
	                ", etiquette=" + etiquette +
	                '}';
	    }
	}

