package aaa;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.List;
import java.util.Locale;  
import org.jfree.data.statistics.Statistics;
public class TempAnalysis {

public static void main(String[] args) throws ParseException, IOException {
String csvFile = "C:\\Users\\asus\\Desktop\\tempfull.csv";  //address of the file
String line = ""; // initialize empty 
String cvsSplitBy = ",";

ArrayList<String> Temperature = new ArrayList<String>();   

ArrayList<String> Date = new ArrayList<String>();       // date as a string with time zone


ArrayList<String> FinalDate = new ArrayList<String>();  // date as a string without time zone


try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
	
	while ((line = br.readLine()) != null) {   // loop through the entire file
		// use comma as separator
		String[] temp = line.split(cvsSplitBy); // each line is an array of csv values
        
		Temperature.add(temp[1]) ;
		Date.add(temp[3]); 
	
	}// end while

	        } catch (IOException e) {
	            e.printStackTrace();
	        }// end catch
//////////////////////////////////////////////////////////////////////////////////////////////
Temperature.remove(0);

///////////////////////////////////////////////////////////////////////////////////////////
///////////////////// loop to initialize final date 
//////////////////////////////////////////////////////////////////////////////////////////
for(int j = 1; j < Date.size(); j++){ // loop through all the array except title
	String finaldate= "" ;    // null string
	for (int x = 0; x < 19; x++){    // loop through the string character
		char c = Date.get(j).charAt(x) ; // we loop to extract that characeter
		String cstr = String.valueOf(c);
		finaldate = finaldate.concat(cstr) ; // concatinate thos 2 string
    							}// end inner for
	FinalDate.add(finaldate);
}// end outter for
///////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////////
////////////////// loop to convert Strings into Date   /////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
// array to store values
ArrayList<Date> DateType = new ArrayList<Date>();

// Parsing loop from final date
for(int y = 0; y < FinalDate.size(); y++){
Date date1 =new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse(FinalDate.get(y));
DateType.add(date1);
}

for(int z = 0; z < FinalDate.size(); z++){
// anonymous instanciatiation	
System.out.println(new SimpleDateFormat("MM-dd-yyyy HH:mm:ss").format(DateType.get(z)));
}// end printing loop


///////////////////////////////////////////////////////////////////////////////////////////

for(int w = 0; w < FinalDate.size(); w++){
System.out.println(Temperature.get(w));      // system temperature
}// end printing loop

//////////////////////////////////////////////////////////////////////////////////////////
///////////////////////  Writting to CSV     ////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
String csvFileW ="C:\\Users\\asus\\Desktop\\new.csv";
FileWriter writer = new FileWriter(csvFileW);
DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

//CSVUtils.writeLine(writer, Arrays.asList("Date", "Temperature"));

for (int m = 0 ; m < Temperature.size(); m++) {

    List<String> list = new ArrayList<>();
    list.add(df.format(DateType.get(m))); // date in the specific format
    list.add(String.valueOf(Temperature.get(m)));
    CSVUtils.writeLine(writer, list);

	
}// end for loop

writer.flush();
writer.close();

//////////////////////////////////////////////////////////////////////////////////////////
/////// /////////////////     Convert Temperature to Double  /////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////
//array to store values
ArrayList<Double> DTemperature = new ArrayList<Double>();

//Parsing loop from final date
for(int y = 0; y < Temperature.size(); y++){
double dtemp =(double)Double.valueOf(Temperature.get(y));
DTemperature.add(dtemp);
}


//////////////////////////////////////////////////////////////////////////////////////////
////////////////////      Statistical summary           //////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////
double mean = Statistics.calculateMean(DTemperature);
double median = Statistics.calculateMedian(DTemperature);


System.out.println("the mean is : "+mean);

System.out.println("the median is : "+median);



	    }// end main

	}// end class