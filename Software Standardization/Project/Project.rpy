I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 99bb5a4d-7914-4561-a28f-19c5758bc12b;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 1;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "Project";
	- _objectCreation = "21650321182023212322332";
	- _umlDependencyID = "2242";
	- _lastID = 3;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "RequirementsPkg.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "RequirementsPkg";
		- _id = GUID ba3c6859-b3a4-4198-856f-258f98fde8c2;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID f79d7b69-407e-4c63-9a43-b42b551009e5;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 10;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ ISubsystem 
			- fileName = "RequirementsPkg";
			- _id = GUID ba3c6859-b3a4-4198-856f-258f98fde8c2;
		}
		{ ISubsystem 
			- fileName = "AnalysisPkg";
			- _id = GUID c81ac6c9-d128-4150-85c4-ba9305ab521e;
		}
		{ ISubsystem 
			- fileName = "ArchitecturePkg";
			- _id = GUID 88d87746-b6b8-4c73-9532-e986e843d144;
		}
		{ ISubsystem 
			- fileName = "SubsystemsPkg";
			- _id = GUID db05e0f7-c24a-4010-b8ed-d446cf2af00e;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 4e02b6d8-302a-4b50-b25c-8eecfed21a40;
			- _myState = 8192;
			- _name = "Model1";
			- _objectCreation = "21712921182023212259732";
			- _umlDependencyID = "2079";
			- _lastModifiedTime = "3.5.2023::15:40:35";
			- _graphicChart = { CGIClassChart 
				- _id = GUID db7df806-ed51-402a-940a-324ba9db9c24;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 4e02b6d8-302a-4b50-b25c-8eecfed21a40;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 1;
				{ CGIClass 
					- _id = GUID 902d2c22-5697-4c8a-94dd-3e74532c1184;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "RequirementsPkg.sbs";
						- _subsystem = "RequirementsPkg";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 274dd457-936f-4c34-ab2c-804f20933a30;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 902d2c22-5697-4c8a-94dd-3e74532c1184;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "RequirementsPkg.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "RequirementsPkg";
				- _id = GUID ba3c6859-b3a4-4198-856f-258f98fde8c2;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID f79d7b69-407e-4c63-9a43-b42b551009e5;
		}
	}
}

