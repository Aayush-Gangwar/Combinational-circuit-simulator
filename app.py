import streamlit as st
import Circuit_simulator
import pickle
import pandas as pd
# import csv
st.title("Combinational circuit simulator")
def main():
    input_file=st.file_uploader("Upload a circuit file",type=".txt",accept_multiple_files=False)
    if(input_file!=None):
        bytes_data=input_file.readlines()
        f=open("samplefile.txt","w")
        for k in bytes_data:
            p=k.decode("utf-8")
            f.write(p)
        f.close()
        p=open("samplefile.txt","r")
        p2=open("samplefile2.txt","w")
        l=p.readlines()
        for k in range(len(l)):
            if(k%2!=0):
                pass
            else:
                p2.write(l[k])

        p.close()
        p2.close()
        if(st.button("Simulate")):
            output_index,input_index=Circuit_simulator.main_run()
            col1, col2 = st.columns(2)
            inputs=open("Input.txt","r")
            txt_content1=(inputs.readlines())
            df={}
            df_={}
            for k in range(len(txt_content1)):
                df[k]=(txt_content1[k]).split()
            
            for k in range(len(txt_content1)):
                df_[k]="Input "+str(input_index[k])
                
            df=pd.DataFrame(df.values())
            df_=pd.DataFrame(df_.values(),columns=["Input_index"])
            df3=pd.concat([df_,df],axis=1)
            st.dataframe(df3)
            csv=df3.to_csv()


            outputs=open("output.txt","r")
            txt_content2=(outputs.readlines())
            df2={}
            df_2={}
            for k in range(len(txt_content2)):
                df2[k]=(txt_content2[k]).split()
            
            for k in range(len(txt_content2)):
                df_2[k]="Output "+str(output_index[k])
                
            df2=pd.DataFrame(df2.values())
            df_2=pd.DataFrame(df_2.values(),columns=["Output_index"])
            df4=pd.concat([df_2,df2],axis=1)
            st.dataframe(df4)
            csv2=df4.to_csv()
            with col1:
                st.download_button("Download_inputs",data=csv,file_name="Inputs.txt")
            with col2:
                st.download_button("Download_Outputs",data=csv2,file_name="Outputs.txt")



    

if __name__=="__main__":
    main()