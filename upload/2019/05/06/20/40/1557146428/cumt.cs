using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
namespace Spider_db
{
    #region Cumt
    public class Cumt
    {
        #region Member Variables
        protected string _accidentName;
        protected string _country;
        protected string _province;
        protected string _accidentClass;
        protected string _accidentType;
        protected string _accidentDate;
        protected string _accidentDescription;
        #endregion
        #region Constructors
        public Cumt() { }
        public Cumt(string accidentName, string country, string province, string accidentClass, string accidentType, string accidentDate, string accidentDescription)
        {
            this._accidentName=accidentName;
            this._country=country;
            this._province=province;
            this._accidentClass=accidentClass;
            this._accidentType=accidentType;
            this._accidentDate=accidentDate;
            this._accidentDescription=accidentDescription;
        }
        #endregion
        #region Public Properties
        public virtual string AccidentName
        {
            get {return _accidentName;}
            set {_accidentName=value;}
        }
        public virtual string Country
        {
            get {return _country;}
            set {_country=value;}
        }
        public virtual string Province
        {
            get {return _province;}
            set {_province=value;}
        }
        public virtual string AccidentClass
        {
            get {return _accidentClass;}
            set {_accidentClass=value;}
        }
        public virtual string AccidentType
        {
            get {return _accidentType;}
            set {_accidentType=value;}
        }
        public virtual string AccidentDate
        {
            get {return _accidentDate;}
            set {_accidentDate=value;}
        }
        public virtual string AccidentDescription
        {
            get {return _accidentDescription;}
            set {_accidentDescription=value;}
        }
        #endregion
    }
    #endregion
}